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
    // 완료하면 줄 긋기, 줄 그어져있으면 줄 지우기
    async updateLine(todo) {
      const data = {
        text: todo.text,
        line: !(todo.line),
      }
      // 완료했는지 데이터 저장
      await axios.put(url + `${todo.id}`, data)
          .then((res) => {
            console.log(res)
            todo.line = !(todo.line)
          })
          .catch((err) => {
            console.log(err)
          })
    },
    // 투두 DELETE
    async deleteTodo(id) {
      await axios.delete(url+`${id}`)
          .then((res)=>{
            console.log(res)
            // 지우면 그부분 자르기
            this.todoList.splice(this.idx,1)
          })
          .catch((err)=>{
            console.log(err)
          })
    },
    // update 하게 되면 false -> true
    updateTodo(){
      this.update = !this.update
    },
    // update 완료시 true -> false로 바꾸고 데이터 수정
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