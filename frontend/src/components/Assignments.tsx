import React, { useEffect, useState } from 'react'
import { Box, Heading, VStack, Checkbox, Text } from '@chakra-ui/react'
import type { Assignment } from '../types'

// DTO as returned by backend (snake_case)
type AssignmentDTO = {
  id: number
  course_id: string
  title: string
  due_date: string
  status: 'pending' | 'completed'
}

export default function Assignments() {
  const [assignments, setAssignments] = useState<Assignment[]>([])

  useEffect(() => {
    const fetchAssignments = async () => {
      try {
        const res = await fetch('/api/assignments')
        if (!res.ok) throw new Error('Network error')
        const data: AssignmentDTO[] = await res.json()
        setAssignments(
          data.map((a: AssignmentDTO): Assignment => ({
            id: a.id,
            courseId: a.course_id,
            title: a.title,
            dueDate: a.due_date,
            status: a.status,
          }))
        )
      } catch (err) {
        // eslint-disable-next-line no-console
        console.error('Failed to fetch assignments', err)
      }
    }
    fetchAssignments()
  }, [])

  return (
    <Box p={4} borderWidth="1px" borderRadius="lg">
      <Heading size="md" mb={4}>Assignments</Heading>
      <VStack spacing={3} align="stretch">
  {assignments.map((a: Assignment) => (
          <Box key={a.id} p={3} bg="gray.50" borderRadius="md" display="flex" alignItems="center">
            <Checkbox isChecked={a.status === 'completed'} mr={3} />
            <VStack align="start" spacing={0}>
              <Text fontWeight="bold">{a.title}</Text>
              <Text fontSize="sm" color="gray.500">Due: {new Date(a.dueDate).toLocaleDateString()}</Text>
            </VStack>
          </Box>
        ))}
      </VStack>
    </Box>
  )
}
