new Vue({
	el : "#vue-app",
	data : {
		age : 25,
		x : 0,
		y : 0
	},
	methods : {
		logName: function(){
			console.log("You entered your name");
		},
		logAge: function(){
			console.log("You entered your age");
		}
	}
})