function getToDivision(divID) {
	var isSmoothScrollSupported = 'scrollBehavior' in document.documentElement.style;

	var ele = document.getElementById(divID);
	var distance = 0;
	while (ele) {
		distance += ele.offsetTop;
		ele = ele.offsetParent;
	}
	distance = distance - 30;

	var options = {
		"behavior": "smooth",
		"left": 0,
		"top": distance
	};

	if (isSmoothScrollSupported) {
		window.scrollTo(options);
	}
	else {
		var current = document.getElementById("body").scrollTop;
		var difference = distance - current;

		var num = current;
		if (difference >= 0) {
			var intr = setInterval(function () {
				window.scrollBy(0, 5);
				num += 5;
				if (num > distance) clearInterval(intr);
			}, 0.5);
		}
		else {
			var num = current;
			var intr = setInterval(function () {
				window.scrollBy(0, -5);
				num -= 5;
				if (num < distance) clearInterval(intr);
			}, 0.5);
		}
	}
}

/*
<a href="javascript:void(0);" onclick="getToDivision('aboutUs');">About Us</a>

<article class="aboutUs" id="aboutUs">
	<h1>What is RuBEC?</h1>
	<p>
		RuBEC(Rungta Business And Entrepreneurship Cell) is an incubation centre under the joint venture of NEN (WADHWANI FDN) & SANTOSH RUNGTA GROUP OF INSTITUTION (R1) Bhilai.
	</p>
	<p>
		Innovative ideas are always appreciated but even after being knowledgeable If you fear to step out of the crowd and face the world the knowledge you have is of no use . In RuBEC E-cell there is "Creation of doers not watchers" and the main mission of the E cell is to develope the brilliant minds such that they create opportunity not only for them but also for people around them and the people around the entire globe 🌍 . We provide the "STEPS TO FLY". RuBEC E-Celll is setup with a primary motive to provide entrepreneurial ecosystem to the young innovative minds where their ideas are given wings.
	</p>
</article>
*/