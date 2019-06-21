new Vue({
	el : "#vue-app",
	data : {
		name : "Jitendra",
		job : "Developer"
	},
	methods : {
		wish : function(){
			return "Good "
		},
		greet: function(time){
			return this.wish() + time + " " + this.name;
		}
	}
});