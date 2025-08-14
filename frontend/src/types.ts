export interface Course {
  id: string
  name: string
  icon: string
}

export interface Assignment {
  id: number
  courseId: string
  title: string
  dueDate: string
  status: 'pending' | 'completed'
}

export interface TodoItem {
  id: string
  text: string
  completed: boolean
}

export interface ScheduleEvent {
  id: string
  title: string
  startTime: string
  endTime: string
  courseId: string
}
