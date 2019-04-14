<template>
  <div class="row">
    <div class="col-md-8">
      <edit-profile-form :model="model">
      </edit-profile-form>
    </div>
    <div class="col-md-4">
      <user-card :user="user"></user-card>
    </div>
  </div>
</template>
<script>
  import EditProfileForm from './Profile/EditProfileForm';
  import UserCard from './Profile/UserCard'
  export default {
    components: {
      EditProfileForm,
      UserCard
    },
    data() {
      return {
        model: {
          company: 'Mary\'s Grill',
          email: 'm.jones@mikesgrill.com',
          username: 'mary123',
          firstName: 'Mary',
          lastName: 'Jones',
          address: '3030 Saint Paul St, Baltimore MD, 21218',
          city: 'Baltimore',
          country: 'USA',
          about: 'Local Baltimore restaurant owner.'
        },
        user: {
          fullName: 'Mary Jones',
          title: 'Ceo/Co-Founder',
          description: `Difficult roads often lead to beautiful destination`,
        }
      }
    }
  }
</script>
<style>
</style>
