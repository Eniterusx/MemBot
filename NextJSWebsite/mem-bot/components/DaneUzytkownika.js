import { Typography, Avatar, Skeleton, ListItemAvatar, ListItem, ListItemText, Menu, Button, MenuItem, ListItemIcon } from '@mui/material'
import LogoutIcon from '@mui/icons-material/Logout';
import Person from '@mui/icons-material/Person'
import { generateDiscordLoginURL } from '../discord'
import React from 'react'
import { useRouter } from 'next/router'
import { destroyCookie } from 'nookies'

import { SessionContext } from '../pages/_app'

export default function DaneUzytkownika (props) {
  const router = useRouter()

  const sesCtx = React.useContext(SessionContext)
  const {data, mutate} = sesCtx

  const [anchorEl, setAnchorEl] = React.useState()

  const logout = () => {
    destroyCookie(null, 'session')
    // mutate()
    router.reload()
    setAnchorEl()
  }

  // Wczytywanie danych
  if (!data) return (<Skeleton sx={{ align: 'center' }} variant='rectangular' animation="wave" width='5vw' height='50px' />);

  // Typ jest zalogowany
  if (data.user_id) {
    return (
       // <Box sx={{ mx: 0 }} style={{width: 75 + data.nickname.length * 11}} boxShadow='10px 10px 10px #000000' elevation={3} backgroundColor='#1976d2' borderRadius='10px'>
       <>
        <Button variant='contained' elevation={3} onClick={(e) => setAnchorEl(e.currentTarget)} sx={{ boxShadow: '10px 10px 10px #000000!important', borderRadius: '10px', backgroundColor: '#1976d2', width: 'auto', display: 'inline-flex', ml: 2, mr: '35%' }}>
          <ListItem>
              <ListItemAvatar>
                <Avatar sx={{ ml: -1.3, width: '30px', height: '30px' }} src={data.avatar}>?</Avatar>
              </ListItemAvatar>
              <ListItemText
                sx={{ ml: -2 }}
                primary={(<Typography sx={{ color: 'white' }}>{data.nickname}</Typography>)}
              />
          </ListItem>
        </Button>
        <Menu
          anchorEl={anchorEl}
          open={Boolean(anchorEl)}
          onClose={() => setAnchorEl()}
          anchorOrigin={{
            vertical: 'bottom',
            horizontal: 'right',
          }}
          transformOrigin={{
            vertical: 'top',
            horizontal: 'right',
          }}
        >
          <MenuItem onClick={logout}>
            <ListItemIcon>
                <LogoutIcon />
            </ListItemIcon>
            <Typography variant="body2" color="text.secondary">
                Wyloguj
            </Typography>
          </MenuItem>
        </Menu>
      </>
    )
  }
  
  return (<Button sx={{ boxShadow: '10px 10px 10px #000000!important', ml: 2, mr: '35%' }} variant='contained' startIcon={<Person />} href={generateDiscordLoginURL()}>Zaloguj</Button>)
}