<template>
  <table cellpadding="10px">
    <tr>
        <th>
          <h3>Start Date:</h3>
        </th>
        <th>
          <date-picker :inline="true"
                     :bootstrap-styling="true"
                     class="testingthis">
          </date-picker>
        </th>
        <th>
          <h3>End Date:</h3>
        </th>
        <th>
          <date-picker :inline="true"
                       :bootstrap-styling="true"
                       class="testingthis">
          </date-picker>
        </th>
        <th>
          <input @click="showModal = !showModal" style="height:30px; width:100px; float:right; background-color:#FF00FF; border-radius:8px; border-color:#BA55D3; border-width:1px; color:#FFFFFF; font-weight:600;" type="submit" value="Submit">
        </th>
    </tr>

      <base-table :columns="inventory_columns"
                  thead-classes="text-primary">
      </base-table>
  </table>
</template>
<script>
  import { BaseTable } from "@/components";
  import DatePicker from 'vuejs-datepicker';
  export default {
    components: {
      BaseTable,
      DatePicker
    },
    computed: {
      inventory_columns(){
        return ["Item", "Quantity"]
      }
    }
  }
</script>
<style>
  .testingthis > div > div {
    background-color: #14B570;
  }
</style>
