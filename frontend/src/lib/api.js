const BASE_URL = "/api";

export async function getTodos() {
  const res = await fetch(`${BASE_URL}/todos/`);
  return await res.json();
}

export async function addTodo(title) {
  const res = await fetch(`${BASE_URL}/todos/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  return await res.json();
}

export async function getPosts() {
  const res = await fetch(`${BASE_URL}/posts/`);
  return await res.json();
}

export async function createPost(post) {
  const res = await fetch(`${BASE_URL}/posts/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(post)
  });
  return await res.json();
}