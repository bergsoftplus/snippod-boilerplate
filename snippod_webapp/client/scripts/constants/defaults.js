'use strict';

var Defaults = {

  route: '/',

  apiPath: '/api/v1',

  page: {
    title: 'Home',
    description: 'Page Component - default',
    keywords: null,
    location: '/',
    returnpage: null,
    transition: null
  },

  account: {
    id:'',
    email: '',
    username: '',
    firstName: '',
    lastName: ''
  },

  auth: {
    loggedIn: false,
    language: 'en-us'
  },

  globalMessages: {
    overlayMessages: null,
    info: null,
    success: null,
    errors: null
  },

  componentMessages: {
    progressed: null,
    completed: null,
    failed: null
  },

  topic: {
    tid: 'root',
    name: 'Snippod Root',
    description: 'Hello, This is Snippod\'s main page. Also, this is boilerpalte for Snippod service.',
    creator: 'snippod'
  },

  snips: {
    posts: [],
    currentPage: 1,
    nextPage: true,
    sortOptions: {
      currentValue: 'upvotes',
      values: {
        'upvotes': 'upvotes',
        'newest': 'time',
        'comments': 'commentCount'
      }
    }
  }



};

module.exports = Defaults;
