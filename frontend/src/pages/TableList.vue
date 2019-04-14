<template>
    <div class="row">
      <div class="col-12">
        <card :title="table1.title">
          <div class="table-responsive">
            <base-table :data="table1.data"
                        :columns="table1.columns"
                        thead-classes="text-primary">
            </base-table>
          </div>
        </card>
      </div>

      <div class="col-12">
        <card class="card-plain">
          <div class="table-full-width table-responsive">
            <base-table :title="table2.title" :sub-title="table2.subTitle" :data="table2.data"
                         :columns="table2.columns">

            </base-table>
          </div>
        </card>
      </div>

    </div>
</template>
<script>
import { BaseTable } from "@/components";
const tableColumns = ["Name", "Supplier", "SKU", "Price"];
const tableData = [
  {
    id: 1,
    name: "NY Strip Sirloin (20 lbs)",
    price: "$367.63",
    supplier: "Porter's Meats",
    sku: "KS944RUR",
  },
  {
    id: 2,
    name: "Loin Pork Chops (10 lbs)",
    price: "$120.42",
    supplier: "Porter's Meats",
    sku: "KS942XUU"
  },
  {
    id: 3,
    name: "Maine Lobster (6 lbs)",
    price: "$88.50",
    supplier: "Phillips Seafood",
    sku: "SF8829BM"
  },
  {
    id: 4,
    name: "King Crab (8 lbs)",
    price: "$74.22",
    supplier: "Phillips Seafood",
    sku: "SF9910BM"
  },
  {
    id: 5,
    name: "Shrimp (12 lbs)",
    price: "$124.80",
    supplier: "Phillips Seafood",
    sku: "SF6366BM"
  },
  {
    id: 6,
    name: 'Produce - Veg (25 lbs)',
    price: '$325.16',
    supplier: 'Prima Foods Inc.',
    sku: 'GNF86700'
  },
  {
    id: 7,
    name: 'Assorted Spirits (20 L)',
    price: '$418.99',
    supplier: 'Hampdem Brewery',
    sku: 'HL1028HD'
  }
];

export default {
  components: {
    BaseTable
  },
  data() {
    return {
      table1: {
        title: "Inventory Pricepoints",
        columns: [...tableColumns],
        data: [...tableData]
      },
      table2: {
        title: "Table on Plain Background",
        columns: [...tableColumns],
        data: [...tableData]
      }
    };
  }
};
</script>
<style>
</style>
