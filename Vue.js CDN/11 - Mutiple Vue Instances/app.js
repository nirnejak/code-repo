var one = new Vue({
	el : "#vue-app-one",
	data : {
		title: 'Vue App One'
	},
	methods : {
		
	},
	computed : {
		greet : function(){
			return "Hello from app one :)"
		}
	}
});

var two = new Vue({
	el : "#vue-app-two",
	data : {
		title: 'Vue App Two'
	},
	methods : {
		changeTitleOne: function(){
			one.title = "New Title Changed by app two";
		}
	},
	computed : {
		greet : function(){
			return "Yo dudes this is app two speaking to ya ;)";
		}
	}
});