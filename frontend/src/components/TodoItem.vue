<template>
  <div>
    <div v-if="update">
      <span @click="updateLine(todo)" :class="{ line:todo.line }">{{todo.text}}</span>
      <button @click="updateTodo()">✏️</button>
      <button @click="deleteTodo(todo.id)">❌</button>
    </div>
    <div v-else>
      <input type="text" v-model="todo.text" @keypress.enter="updateTodo(todo.id)">
      <button @click="updateComplete(todo)">완료</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
let url = 'https://jihyeon.pythonanywhere.com/api/todo/'

export default {
  data() {
    return {
      update: true,
    }
  },
  props: {
    todoList: [Array, Object],
    todo: [Array, Object],
    idx: Number,
  },
  methods: {
    async updateLine(todo) {
      const data = {
        text: todo.text,
        line: !(todo.line),
      }
      await axios.put(url + `${todo.id}`, data)
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      todo.line = !(todo.line)
    },
    async deleteTodo(id) {
      await axios.delete(url+`${id}`)
          .then((res)=>{
            console.log(res)
            this.todoList.splice(this.idx,1)
          })
          .catch((err)=>{
            console.log(err)
          })
    },
    updateTodo(){
      this.update = !this.update
    },
    async updateComplete(todo){
      this.update = !this.update
      const data = {
        text: todo.text,
        line: todo.line,
      }
      await axios.put(url+`${todo.id}`,data)
          .then((res)=>{
            console.log(res)
          })
          .catch((err)=>{
            console.log(err)
          })
    }
  }
}
</script>