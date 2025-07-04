const AUTH_URL = "http://auth:8001";
const TODO_URL = "http://todo:8002";
const BOARD_URL = "http://board:8003";

// ✅ 로그인
export async function login(username, password) {
  const res = await fetch(`${AUTH_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  return await res.json();
}

// ✅ 투두 목록
export async function getTodos() {
  const res = await fetch(`${TODO_URL}/todos/`);
  return await res.json();
}

// ✅ 투두 추가
export async function addTodo(title) {
  const res = await fetch(`${TODO_URL}/todos/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  return await res.json();
}

// ✅ 게시글 목록
export async function getPosts() {
  const res = await fetch(`${BOARD_URL}/posts/`);
  return await res.json();
}

// ✅ 게시글 작성
export async function createPost(post) {
  const res = await fetch(`${BOARD_URL}/posts/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(post),
  });
  return await res.json();
}
