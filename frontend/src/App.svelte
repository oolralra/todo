<script>
  import { onMount } from 'svelte';
  import { getTodos, addTodo } from './lib/api.js';

  let todos = [];
  let newTitle = '';

  onMount(async () => {
    todos = await getTodos();
  });

  async function handleAdd() {
    if (!newTitle.trim()) return;
    const todo = await addTodo(newTitle);
    todos = [...todos, todo];
    newTitle = '';
  }
</script>

<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 2rem;
  }

  h1 {
    font-size: 2rem;
    color: #333;
  }

  .todo-input {
    margin-top: 1rem;
    display: flex;
    gap: 0.5rem;
  }

  input {
    flex: 1;
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 6px;
  }

  button {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }

  button:hover {
    background-color: #45a049;
  }

  ul {
    margin-top: 1.5rem;
    padding: 0;
    list-style: none;
  }

  li {
    background: white;
    padding: 0.75rem;
    margin-bottom: 0.5rem;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  }
</style>

<h1>fastapi 할 일 목록</h1>

<div class="todo-input">
  <input bind:value={newTitle} placeholder="할 일 입력" />
  <button on:click={handleAdd}>추가</button>
</div>

<ul>
  {#each todos as todo}
    <li>{todo.title} {todo.completed ? '✅' : ''}</li>
  {/each}
</ul>

