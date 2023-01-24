import {
  Box
} from '@mui/material'

import React from 'react'

const ModalBox = (props, ref) => {
  return (
    <Box
      sx={{
        position: 'Absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 'min(80vw, 600px)',
        bgcolor: 'background.default',
        borderRadius: 1,
        boxShadow: 24,
        p: 4
      }}
      ref={ref}
      {...props}
    />
  )
}

export default React.forwardRef(ModalBox)
