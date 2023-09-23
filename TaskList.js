import React, { useState } from 'react';
import './TaskList.css';
const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [currentTasks, setCurrentTasks] = useState([]);
  const [completedTasks, setCompletedTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  const addTask = () => {
    if (newTask.trim() !== '') {
      setTasks([...tasks, newTask]);
      setNewTask('');
    }
  };
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      addTask();
    }
  }

  const removeTask = (index) => {
    const updatedTasks = tasks.filter((_, i) => i !== index);
    setTasks(updatedTasks);
  };

  const removeCurrentTask = (index) => {
    const updatedTasks = currentTasks.filter((_, i) => i !== index);
    setCurrentTasks(updatedTasks);
  };

  const removeCompletedTask = (index) => {
    const updatedTasks = completedTasks.filter((_, i) => i !== index);
    setCompletedTasks(updatedTasks);
  };

  const moveToCompleted = (index) => {
    const taskToMove = currentTasks[index];
    const updatedTasks = currentTasks.filter((_, i) => i !== index);
    setCurrentTasks(updatedTasks);
    setCompletedTasks([...completedTasks, taskToMove]);
  }

  const moveToCurrent = (index) => {
    const taskToMove = tasks[index];
    const updatedTasks = tasks.filter((_, i) => i !== index);
    setTasks(updatedTasks);
    setCurrentTasks([...currentTasks, taskToMove]);
  }

  const moveToAll = (index) => {
    const taskToMove = completedTasks[index];
    const updatedTasks = completedTasks.filter((_, i) => i !== index);
    setCompletedTasks(updatedTasks);
    setTasks([...tasks, taskToMove]);
  }
  return (
    <div className="task-list-container">
      <div className="task-list">
        <h2>Tasks</h2>
        <div>
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            onKeyUp={handleKeyPress}
          />
          <button onClick={addTask}>Add Task</button>
        </div>
        <ul>
          {tasks.map((task, index) => (
            <li key={index}>
              {task}{' '}
              <button onClick={() => moveToCurrent(index)}>Start</button>
              <button onClick={() => removeTask(index, 'tasks')}>x</button>{' '}
            </li>
          ))}
        </ul>
      </div>
      <div className="task-list">
        <h2>Current Tasks</h2>
        <ul>
          {currentTasks.map((task, index) => (
            <li key={index}>
              {task}{' '}
              <button onClick={() => moveToCompleted(index, 'completedTasks')}>Finish</button>
              <button onClick={() => removeCurrentTask(index, 'currentTasks')}>x</button>
            </li>
          ))}
        </ul>
      </div>
      <div className="task-list">
        <h2>Completed Tasks</h2>
        <ul>
          {completedTasks.map((task, index) => (
            <li key={index}>
              {task}{' '}
              <button onClick={() => moveToAll(index, 'completedTasks')}>←</button>
              <button onClick={() => removeCompletedTask(index, 'completedTasks')}>x</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default TaskList;
