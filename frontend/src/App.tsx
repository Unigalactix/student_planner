import React from 'react'
import { Container, Heading } from '@chakra-ui/react'
import Assignments from './components/Assignments'

export default function App() {
  return (
    <Container maxW="container.lg" py={6}>
      <Heading mb={6}>Student Planner (frontend scaffold)</Heading>
      <Assignments />
    </Container>
  )
}
