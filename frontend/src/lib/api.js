const BASE_URL = "http://backend:8000";

export async function getTodos() {
  const res = await fetch(`${BASE_URL}/todos`);
  return await res.json();
}

export async function addTodo(title) {
  const res = await fetch(`${BASE_URL}/todos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  return await res.json();
}
