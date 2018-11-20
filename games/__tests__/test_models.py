from unittest.mock import patch

import pytest
from django.utils import timezone

from profiles.__tests__.factories import ProfileFactory
from ..constants import ADVENTURE_TYPE_OTHER
from .factories import AdventureFactory, GameSessionFactory, GameSessionPlayerSignUpFactory

from pytest_factoryboy import register

register(AdventureFactory)
register(GameSessionFactory)
register(GameSessionPlayerSignUpFactory)
register(ProfileFactory)


@pytest.mark.django_db
def test_factory_fixture(adventure_factory):
    adventure = adventure_factory(type=ADVENTURE_TYPE_OTHER)

    assert adventure.type == ADVENTURE_TYPE_OTHER


@pytest.mark.django_db
def test_other_adventure_display_only_name(adventure_factory):
    adventure = adventure_factory(type=ADVENTURE_TYPE_OTHER)

    assert str(adventure) == 'Super Adventure'


@pytest.mark.django_db
def test_future_game_session_not_ended(game_session_factory):
    # given
    game = game_session_factory(date=timezone.now().date() + timezone.timedelta(days=2))

    # then
    assert not game.ended


@pytest.mark.django_db
def test_past_game_session_ended(game_session_factory):
    # given
    game = game_session_factory(date=timezone.now().date() - timezone.timedelta(days=2))

    # then
    assert game.ended


@pytest.mark.django_db
def test_today_after_time_end_game_session_is_ended(game_session_factory):
    # given
    game = game_session_factory(date=timezone.now().date(),
                                time_end=(timezone.now() - timezone.timedelta(hours=2)).time())

    # then
    assert game.ended


@pytest.mark.django_db
@patch('games.models.send_email')
def test_minimum_players_not_available_email_sent(send_email_function_mock, game_session_factory, profile_factory,
                                                  game_session_player_sign_up_factory):
    # given
    game = game_session_factory(dm=profile_factory())
    game_session_player_sign_up_factory.create_batch(2, game=game, player=profile_factory())

    # when
    game.checkMinimumPlayers()

    # then
    # assert game.players.count() == 3
    assert send_email_function_mock.called


@pytest.mark.django_db
@patch('games.models.send_email')
def test_minimum_players_number_is_there_no_email(send_email_function_mock, game_session_factory, profile_factory,
                                                  game_session_player_sign_up_factory):
    # given
    game = game_session_factory(dm=profile_factory())
    game_session_player_sign_up_factory.create_batch(3, game=game, player=profile_factory())

    # when
    game.checkMinimumPlayers()

    # then
    # assert game.players.count() == 3
    assert not send_email_function_mock.called
