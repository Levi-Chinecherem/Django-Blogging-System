window.addEventListener("DOMContentLoaded",() => {
	const clock = new MotionClock(".clock");
});

class MotionClock {
	constructor(qs) {
		const el = document.querySelector(qs);
		const msInSec = 1000;
		const msInMin = msInSec * 60;
		const msInHr = msInMin * 60;
		const msInDay = msInHr * 24;
		const date = new Date();

		let time = date.getHours() * msInHr;
		time += date.getMinutes() * msInMin;
		time += date.getSeconds() * msInSec;
		time += date.getMilliseconds();

		if (el) {
			const handCl = ".clock__hand";
			const hr = el.querySelector(`${handCl}--hr`);
			const min = el.querySelector(`${handCl}--min`);
			const sec = el.querySelector(`${handCl}--sec`);

			if (hr) {
				const hrDelay = (msInDay * ((time % msInDay) / msInDay)) / msInSec;
				hr.style.animationDelay = `${-hrDelay}s`;
			}
			if (min) {
				const minDelay = (msInHr * ((time % msInHr) / msInHr)) / msInSec;
				min.style.animationDelay = `${-minDelay}s`;
			}
			if (sec) {
				const secDelay = (msInMin * ((time % msInMin) / msInMin)) / msInSec;
				sec.style.animationDelay = `${-secDelay}s`;

				const trail = sec.querySelectorAll(`${handCl}-trail`);

				if (trail) {
					const msDelay = (time % msInSec) / msInSec;

					Array.from(trail).forEach(t => {
						t.style.animationDelay = `${-msDelay}s`;
					});
				}
			}
		}
	}
}