/* eslint-disable react/prop-types */
'use client'

import {
  Heading,
  Avatar,
  Box,
  Center,
  Text,
  useColorModeValue,
} from '@chakra-ui/react'

export default function Card({avatarLink, name, description}) {
  return (
    <Center py={6}>
      <Box
        maxW={'320px'}
        w={'full'}
        minW="300px"
        maxH="400px"
        bg="#121212"
        boxShadow={'2xl'}
        rounded={'lg'}
        p={6}
        textAlign={'center'}>
        <Avatar
          size={'xl'}
          src={avatarLink}
          mb={4}
          pos={'relative'}
        />
        <Heading fontSize={'2xl'} color="white" fontFamily={'body'}>
          {name}
        </Heading>
        <Text
          textAlign={'center'}
          color={useColorModeValue('white.700', 'white.400')}
          px={3}>
          {description}
        </Text>


      </Box>
    </Center>
  )
}