
<script>
  import { onMount } from 'svelte';
  import { getTodos, addTodo } from './lib/api.js';

  let todos = [];
  let newTitle = '';

  let email = '';
  let password = '';
  let token = '';
  let error = '';

  async function handleLogin() {
    try {
      const res = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });

      if (!res.ok) {
        throw new Error('로그인 실패');
      }

      const data = await res.json();
      token = data.access_token;
      localStorage.setItem('token', token);
      error = '';
      await loadTodos();
    } catch (err) {
      error = err.message;
    }
  }

  async function loadTodos() {
    const storedToken = localStorage.getItem('token');
    if (!storedToken) return;
    const res = await fetch('http://localhost:8000/todos', {
      headers: { Authorization: 'Bearer ' + storedToken }
    });
    todos = await res.json();
  }

  async function handleAdd() {
    if (!newTitle.trim()) return;
    const storedToken = localStorage.getItem('token');
    const res = await fetch('http://localhost:8000/todos', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + storedToken
      },
      body: JSON.stringify({ title: newTitle })
    });
    const todo = await res.json();
    todos = [...todos, todo];
    newTitle = '';
  }

  onMount(loadTodos);
</script>

<style>
  body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 2rem;
  }
  input {
    margin-bottom: 0.5rem;
    padding: 0.5rem;
    font-size: 1rem;
    width: 100%;
    max-width: 300px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  button {
    margin-bottom: 1rem;
    padding: 0.5rem 1rem;
  }
  .error {
    color: red;
  }
</style>

<h1>로그인</h1>
<input placeholder="Email" bind:value={email} />
<input type="password" placeholder="Password" bind:value={password} />
<button on:click={handleLogin}>로그인</button>
{#if error}
  <div class="error">{error}</div>
{/if}

<h2>Todo</h2>
<div class="todo-input">
  <input bind:value={newTitle} placeholder="새 할 일" />
  <button on:click={handleAdd}>추가</button>
</div>
<ul>
  {#each todos as todo}
    <li>{todo.title}</li>
  {/each}
</ul>
