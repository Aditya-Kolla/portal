import React, {Fragment} from 'react';
import LoadingDiv from "../common/LoadingDiv";
import {ClipLoader} from "react-spinners";
import {inject, observer} from "mobx-react";
import Typography from "../../node_modules/@material-ui/core/Typography/Typography";
import withStyles from '@material-ui/core/styles/withStyles';
import Button from "../../node_modules/@material-ui/core/Button/Button";
import {Link} from "react-router-dom";
import List from "../../node_modules/@material-ui/core/List/List";
import ListItem from "../../node_modules/@material-ui/core/ListItem/ListItem";
import ListItemIcon from "../../node_modules/@material-ui/core/ListItemIcon/ListItemIcon";
import ListItemText from "../../node_modules/@material-ui/core/ListItemText/ListItemText";
import Avatar from "../../node_modules/@material-ui/core/Avatar/Avatar";
import Chip from "../../node_modules/@material-ui/core/Chip/Chip";
import CalendarIcon from "@material-ui/icons/Event";
import RoomIcon from "@material-ui/icons/Room";
import Hidden from "../../node_modules/@material-ui/core/Hidden/Hidden";

const styles = theme => ({
  root: {
    padding: '0 20px',
  },
  gameSession: {
    marginBottom: 20,
  },
  actions: {
    display: 'flex',
  },
  chip: {
    marginRight: 10,
    marginBottom: 10,
  },
  title: {
    marginBottom: 10,
  }
});

@withStyles(styles, {withTheme: true})
@inject('portalStore') @observer
export default class Games extends React.Component {

  state = {
    loading: true,
  };

  componentDidMount(){
    this.setState({
      loading: true,
    });
    this.props.portalStore.games.fetch().then(() => {
      this.setState({
        loading: false,
      })
    })
  }

  render() {
    const {classes} = this.props;

    if(this.state.loading)
      return (
          <LoadingDiv>
            <ClipLoader color={'#FFDE00'} loading={this.state.loading}/>
          </LoadingDiv>
        );
    else
        return (
          <div className={classes.root}>
              {this.props.portalStore.games.items.map(game => (
                <Hidden xsDown>
                  {game.adventure && (
                    <Fragment>
                      <List>
                        <ListItem button>
                          <ListItemIcon>
                            <div style={{textAlign: 'center'}}>
                              <Typography variant="title" style={{marginBottom: 0}}>
                                <CalendarIcon/><br/>
                                {game.getDateString()}
                              </Typography>
                              <Typography component='p'>
                                {game.getWeekDay()}<br/>
                                <strong>{game.timeStart}</strong>
                              </Typography>
                            </div>
                          </ListItemIcon>

                          <ListItemText primary={
                            <Typography variant='title' className={classes.title}>
                              {game.adventure.title_display}
                            </Typography>
                          } secondary={
                            <Fragment>
                              <Chip avatar={<Avatar><RoomIcon/></Avatar>} label={game.tableName} className={classes.chip} />
                              <Link to={`/profiles/${game.dm.id}/`}>{game.getDMName()}</Link>
                            </Fragment>
                          } />

                          <ListItemIcon>
                            <Avatar>JK</Avatar>
                          </ListItemIcon>
                          <ListItemIcon>
                            <Avatar>KS</Avatar>
                          </ListItemIcon>
                          <ListItemIcon>
                            <Avatar>+{game.spots}</Avatar>
                          </ListItemIcon>
                        </ListItem>
                      </List>
                    </Fragment>
                  )}
                  {!game.adventure && (
                    <Fragment>
                      <List>
                        <ListItem button>
                          <ListItemIcon>
                            <div style={{textAlign: 'center'}}>
                              <Typography variant="title" style={{marginBottom: 0}}>
                                <CalendarIcon/><br/>
                                {game.getDateString()}
                              </Typography>
                              <Typography component='p'>
                                {game.getWeekDay()}<br/>
                                <strong>{game.timeStart}</strong>
                              </Typography>
                            </div>
                          </ListItemIcon>
                          <ListItemText primary={
                            <Typography variant='title' className={classes.title}>
                              Empty Slot
                            </Typography>
                          } secondary={
                            <Chip avatar={<Avatar><RoomIcon/></Avatar>} label={game.tableName} className={classes.chip} />
                          } />
                          {this.props.portalStore.currentUser.role === 'Dungeon Master' && (
                            <Button variant="outlined" size="small" color="primary">
                              Run a game in this slot
                            </Button>
                          )}
                        </ListItem>
                      </List>
                    </Fragment>
                  )}
                </Hidden>
              ))}
          </div>
        );
  }
}
