new Vue({
	el : "#vue-app",
	data : {
		error: false,
		success: false
	},
	methods : {

	},
	computed : {
		compClasses: function(){
			return {
				available : this.available,
				nearby : this.nearby
			}
		}
	}
})