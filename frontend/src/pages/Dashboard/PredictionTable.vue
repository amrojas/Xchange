<template>
  <div>
    <div>
    <table width="100%">
      <tr>
          <th>
            <h3>Start Date:</h3>
          </th>
          <th>
            <date-picker :inline="true"
                         :bootstrap-styling="true"
                         v-model="start_date"
                         :disabled-dates="start_disabled_dates"
                         :highlighted="highlighted"
                         class="testingthis">
            </date-picker>
          </th>
          <th>
            <h3>End Date:</h3>
          </th>
          <th>
            <date-picker :inline="true"
                         :bootstrap-styling="true"
                         v-model="end_date"
                         :disabled-dates="end_disabled_dates"
                         :highlighted="highlighted"
                         class="testingthis">
            </date-picker>
          </th>
          <th>
            <input v-on:click="compute" style="width:75px; float:right; background-color:#FF00FF; border-radius:8px; border-color:#BA55D3; border-width:1px; color:#FFFFFF; font-weight:600;" type="submit" value="Submit">
          </th>
      </tr>
    </table>
    </div>
    <br>
    <br>
    <div style="width: 100%; text-align: center" >
      <h3 v-if="loading" style="text-align: center">Neural Net Analyzing Your Customer's Needs</h3>
    </div>
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
        loading: false,
        sales: [],
        ingredients: [],
        start_date : new Date(),
        end_date: new Date(),
        start_disabled_dates: {
          to: new Date()
        },
        highlighted: {
          includeDisabled: true
        }
      }
    },
    computed: {
      sales_colunmns(){
        return ["Item", "Quantity"]
      },
      inventory_columns(){
        return ["Ingredient", "Quantity"]
      },
      end_disabled_dates() {
        return {
          to: this.start_date
        }
      }
    },
    methods: {
      compute: function () {
        let value = !this.showTable;
        if (value) {
          this.loading = true;
          axios
            .get('http://0.0.0.0:5000/create-order', {
              params: {
                start_date: String(this.start_date.getFullYear()) + ' ' + String(this.start_date.getMonth() + 1) + ' ' + String(this.start_date.getDate()),
                end_date: String(this.end_date.getFullYear()) + ' ' + String(this.end_date.getMonth() + 1) + ' ' + String(this.end_date.getDate())
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
              this.loading = false;
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

  .testingthis > .vdp-datepicker__calendar > div > .disabled {
    background-color: lightgrey;
  }

  th {
    padding-right: 30px;
  }
</style>
