<template>
  <div>
    <div class="table-full-width">
    <table>
      <tr>
          <th>
            <h3>Start Date:</h3>
          </th>
          <th style="padding-right: 100px">
            <date-picker :inline="true"
                         :bootstrap-styling="true"
                         v-model="start_date"
                         class="testingthis">
            </date-picker>
          </th>
          <th>
            <h3>End Date:</h3>
          </th>
          <th style="padding-right: 150px">
            <date-picker :inline="true"
                         :bootstrap-styling="true"
                         v-model="end_date"
                         class="testingthis">
            </date-picker>
          </th>
          <th>
            <input v-on:click="compute" style="height:30px; width:100px; float:right; background-color:#FF00FF; border-radius:8px; border-color:#BA55D3; border-width:1px; color:#FFFFFF; font-weight:600;" type="submit" value="Submit">
          </th>
      </tr>
    </table>
    </div>
    <br>
    <br>
    <table width="100%" v-if="showTable">
      <tr>
        <th>
          <h3>Predicted Sales:</h3>
        </th>
        <th>
          <h3>Inventory Needs:</h3>
        </th>
      </tr>
      <tr>
        <th width="50%">
          <base-table :columns="sales_colunmns"
                      :data="sales"
                      thead-classes="text-primary">
          </base-table>
        </th>
        <th width="50%">
          <base-table :columns="inventory_columns"
                      :data="ingredients"
                      thead-classes="text-primary">
          </base-table>
        </th>
      </tr>
    </table>

  </div>
</template>
<script>
  import { BaseTable } from "@/components";
  import DatePicker from 'vuejs-datepicker';
  import axios from 'axios';

  export default {
    components: {
      BaseTable,
      DatePicker
    },
    data() {
      return {
        showTable: false,
        sales: [],
        ingredients: [],
        start_date : new Date(),
        end_date: new Date(),
      }
    },
    computed: {
      sales_colunmns(){
        return ["Item", "Quantity"]
      },
      inventory_columns(){
        return ["Ingredient", "Quantity"]
      }
    },
    methods: {
      compute: function () {
        let value = !this.showTable;
        if (value) {
          axios
            .get('http://0.0.0.0:5000/create-order', {
              params: {
                start_date: String(this.start_date.getFullYear()) + ' ' + String(this.start_date.getMonth()) + ' ' + String(this.start_date.getDate()),
                end_date: String(this.end_date.getFullYear()) + ' ' + String(this.end_date.getMonth()) + ' ' + String(this.end_date.getDate())
              }
            })
            .then(response => {
              let data = response.data;
              let sales = Object.entries(data.sales);
              let ingredients = Object.entries(data.ingredients);
              for (let x of sales) {
                this.sales.push({
                  item: x[0],
                  quantity: x[1]
                });
              }
              for (let y of ingredients) {
                this.ingredients.push({
                  ingredient: y[0],
                  quantity: y[1]
                })
              }
              this.showTable = value;
            });
        } else {
          this.ingredients = [];
          this.sales = [];
          this.showTable = value;
        }
      }

    }
  }
</script>
<style>
  .testingthis > div > div {
    background-color: #14B570;
  }

  th {
    padding-right: 30px;
  }
</style>
