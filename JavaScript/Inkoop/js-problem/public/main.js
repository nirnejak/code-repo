new Vue({
  el: "#app",
  data: {
    clients: {},
    totalNoOfCollaborators: null,
    averageCollaborations: null,
    minCollaboratedClient: null,
    maxCollaboratedClient: null,
    totalNoOfClients: null,
    maxCountriesClient: null
  },
  created() {
    axios.get('/data')
      .then(res => {
        this.clients = res.data.clients
        this.totalNoOfCollaborators = res.data.totalNoOfCollaborators
        this.averageCollaborations = res.data.averageCollaborations
        this.minCollaboratedClient = res.data.minCollaboratedClient
        this.maxCollaboratedClient = res.data.maxCollaboratedClient
        this.totalNoOfClients = res.data.totalNoOfClients
        this.maxCountriesClient = res.data.maxCountriesClient

        this.clients = Object.keys(this.clients).map(key => {
          return {
            name: key,
            ...this.clients[key]
          }
        })
      })
      .catch(err => console.log(err))
  },
  methods: {
    sort(option) {
      this.clients.sort((client1, client2) => {
        if (client1[option] > client2[option]) {
          return 1
        } else if (client1[option] < client2[option]) {
          return -1
        }
        return 0
      })
    }
  }
})