import React, { useEffect, useState } from "react";
import { getUsers, addUser, deleteUser } from "./api";
import UserTable from "./components/UserTable";
import UserForm from "./components/UserForm";

export default function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    loadUsers();
  }, []);

  async function loadUsers() {
    try {
      const data = await getUsers();
      setUsers(data.users);
    } catch (err) {
      console.error(err);
    }
  }

  async function handleAdd(user) {
    await addUser(user);
    loadUsers();
  }

  async function handleDelete(id) {
    await deleteUser(id);
    loadUsers();
  }

  return (
    <div>
      <h1>Users</h1>
      <UserForm onAdd={handleAdd} />
      <UserTable users={users} onDelete={handleDelete} />
    </div>
  );
}