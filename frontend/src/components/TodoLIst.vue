<template>
  <div>
    <h1>TodoList</h1>
    <input v-model="newTodo" type="text" @keypress.enter="createTodo">
    <button @click="createTodo">확인</button>
    <div v-for="(todo, idx) in todoList" :key="idx">
      <todo-item :todo="todo" :idx="idx" :todoList="todoList"></todo-item>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import TodoItem from "@/components/TodoItem";
let url = 'https://jihyeon.pythonanywhere.com/api/todo/'
// let url = 'http://127.0.0.1:8000/api/todo/'

export default {
  name: "TodoLIst",
  components: {
    TodoItem,
  },
  data() {
    return {
      todoList: [],
      newTodo: '',
    }
  },
  created() {
    // 로컬스토리지에 저장된 투두 리스트가 있다면 불러온다
    this.getTodoList()
  },
  methods: {
    async getTodoList() {
      const response = await axios.get(url)
      this.todoList = response.data
    },
    postTodo(todo) {
      axios.post(url,todo)
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createTodo() {
      const todo = {
        text: this.newTodo,
        line: false,
      }
      this.postTodo(todo)
      this.newTodo = ''
      this.todoList.push(todo)
      this.getTodoList()
    },
  }
}
</script>

<style>
.line{
  text-decoration: line-through;
}
</style>