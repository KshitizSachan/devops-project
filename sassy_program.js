function sassyResponse() {
    const favoriteNumber = prompt("What's your favorite number? 🤔");
  
    if (!favoriteNumber) {
      console.log("You gotta type something, genius. 🙄");
    } else if (isNaN(favoriteNumber)) {
      console.log("Numbers only, Einstein. Try again. 🙄");
    } else if (favoriteNumber < 0) {
      console.log("A negative number? What a mood. 😒");
    } else if (favoriteNumber == 0) {
      console.log("Zero? Really? Aim higher, my friend. 😑");
    } else if (favoriteNumber > 0 && favoriteNumber < 10) {
      console.log("Cute. A single digit. How original. 😏");
    } else if (favoriteNumber >= 10 && favoriteNumber <= 100) {
      console.log("Playing it safe, I see. 🙃");
    } else {
      console.log("Whoa, big numbers! Compensating for something? 😉");
    }
  }
  
  sassyResponse();
  