<script setup>
import { RouterLink, RouterView } from "vue-router";

import HelloWorld from "./components/HelloWorld.vue";
import TheWelcome from "./components/TheWelcome.vue";
</script>

<template>
  <div class="container mx-auto max-w-3xl px-4 sm:px-6 xl:max-w-5xl xl:px-0">
    <div class="flex flex-col justify-between h-screen">
      <header class="flex flex-row items-center justify-between py-10">
        <div class="nav-logo text-2xl font-bold">
          <router-link to="/" v-if="mySite">{{ mySite.name }}</router-link>
        </div>
        . . .
      </header>
      . . .
    </div>
  </div>
</template>

<script>
import gql from "graphql-tag";

export default {
  data() {
    return {
      mySite: null,
    };
  },

  async created() {
    const siteInfo = await this.$apollo.query({
      query: gql`
        query {
          site {
            name
          }
        }
      `,
    });
    this.mySite = siteInfo.data.site;
  },
};
</script>
<script>
import { SITE_INFO } from "@/queries";

export default {
  data() {
    return {
      mySite: null,
    };
  },

  async created() {
    const siteInfo = await this.$apollo.query({
      query: SITE_INFO,
    });
    this.mySite = siteInfo.data.site;
  },
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
