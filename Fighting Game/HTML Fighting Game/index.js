const canvas = document.querySelector("canvas")
const c = canvas.getContext("2d")

canvas.width = 1024
canvas.height = 576

c.fillRect(0, 0, canvas.width, canvas.height)

const gravity = 0.7

const background = new Sprite({
  position: {
    x: 0,
    y: 0
  },
  imageSrc: "./img/background.png"
})

const shop = new Sprite({
  position: {
    x: 600,
    y: 128
  },
  imageSrc: "./img/shop.png",
  scale: 2.75,
  framesMax: 6
})

const playerCharacter = new Fighter({
  position: {
    x: 0,
    y: 0
  },
  velocity: {
    x: 0,
    y: 0
  },
  offset: {
    x: 0,
    y: 0
  },
  imageSrc: "./img/samuraiMack/Idle.png",
  framesMax: 8,
  scale: 2.5,
  offset: {
    x: 215,
    y: 157
  },
  sprites: {
    idle: {
      imageSrc: "./img/samuraiMack/Idle.png",
      framesMax: 8
    },
    run: {
      imageSrc: "./img/samuraiMack/Run.png",
      framesMax: 8
    },
    jump: {
      imageSrc: "./img/samuraiMack/Jump.png",
      framesMax: 2
    },
    fall: {
      imageSrc: "./img/samuraiMack/Fall.png",
      framesMax: 2
    },
    attack1: {
      imageSrc: "./img/samuraiMack/Attack1.png",
      framesMax: 6
    },
    takeHit: {
      imageSrc: "./img/samuraiMack/Take Hit - white silhouette.png",
      framesMax: 4
    },
    death: {
      imageSrc: "./img/samuraiMack/Death.png",
      framesMax: 6
    }
  },
  attackBox: {
    offset: {
      x: 100,
      y: 50
    },
    width: 160,
    height: 50
  }
})

const playerEnemy = new Fighter({
  position: {
    x: 400,
    y: 100
  },
  velocity: {
    x: 0,
    y: 0
  },
  color: "blue",
  offset: {
    x: -50,
    y: 0
  },
  imageSrc: "./img/kenji/Idle.png",
  framesMax: 4,
  scale: 2.5,
  offset: {
    x: 215,
    y: 167
  },
  sprites: {
    idle: {
      imageSrc: "./img/kenji/Idle.png",
      framesMax: 4
    },
    run: {
      imageSrc: "./img/kenji/Run.png",
      framesMax: 8
    },
    jump: {
      imageSrc: "./img/kenji/Jump.png",
      framesMax: 2
    },
    fall: {
      imageSrc: "./img/kenji/Fall.png",
      framesMax: 2
    },
    attack1: {
      imageSrc: "./img/kenji/Attack1.png",
      framesMax: 4
    },
    takeHit: {
      imageSrc: "./img/kenji/Take hit.png",
      framesMax: 3
    },
    death: {
      imageSrc: "./img/kenji/Death.png",
      framesMax: 7
    }
  },
  attackBox: {
    offset: {
      x: -170,
      y: 50
    },
    width: 170,
    height: 50
  }
})

console.log(playerCharacter)

const keys = {
  a: {
    pressed: false
  },
  d: {
    pressed: false
  },
  ArrowRight: {
    pressed: false
  },
  ArrowLeft: {
    pressed: false
  }
}

decreaseTimer()

function animate() {
  window.requestAnimationFrame(animate)
  c.fillStyle = "black"
  c.fillRect(0, 0, canvas.width, canvas.height)
  background.update()
  shop.update()
  c.fillStyle = "rgba(255, 255, 255, 0.15)"
  c.fillRect(0, 0, canvas.width, canvas.height)
  playerCharacter.update()
  playerEnemy.update()

  playerCharacter.velocity.x = 0
  playerEnemy.velocity.x = 0

  // Player Movement

  if (keys.a.pressed && playerCharacter.lastKey === "a") {
    playerCharacter.velocity.x = -5
    playerCharacter.switchSprite("run")
  } else if (keys.d.pressed && playerCharacter.lastKey === "d") {
    playerCharacter.velocity.x = 5
    playerCharacter.switchSprite("run")
  } else {
    playerCharacter.switchSprite("idle")
  }

  // Jumping
  if (playerCharacter.velocity.y < 0) {
    playerCharacter.switchSprite("jump")
  } else if (playerCharacter.velocity.y > 0) {
    playerCharacter.switchSprite("fall")
  }

  // Enemy Movement
  if (keys.ArrowLeft.pressed && playerEnemy.lastKey === "ArrowLeft") {
    playerEnemy.velocity.x = -5
    playerEnemy.switchSprite("run")
  } else if (keys.ArrowRight.pressed && playerEnemy.lastKey === "ArrowRight") {
    playerEnemy.velocity.x = 5
    playerEnemy.switchSprite("run")
  } else {
    playerEnemy.switchSprite("idle")
  }

  // Enemy Jumping
  if (playerEnemy.velocity.y < 0) {
    playerEnemy.switchSprite("jump")
  } else if (playerEnemy.velocity.y > 0) {
    playerEnemy.switchSprite("fall")
  }

  // Hit Detection
  if (
    rectangularCollision({
      rectangle1: playerCharacter,
      rectangle2: playerEnemy
    }) &&
    playerCharacter.isAttacking &&
    playerCharacter.framesCurrent === 4
  ) {
    playerEnemy.takeHit()
    playerCharacter.isAttacking = false

    gsap.to("#enemyHealth", {
      width: playerEnemy.health + "%"
    })
  }

  // If Player Misses
  if (playerCharacter.isAttacking && playerCharacter.framesCurrent === 4) {
    playerCharacter.isAttacking = false
  }

  // If Player Gets Hit
  if (
    rectangularCollision({
      rectangle1: playerEnemy,
      rectangle2: playerCharacter
    }) &&
    playerEnemy.isAttacking &&
    playerEnemy.framesCurrent === 2
  ) {
    playerCharacter.takeHit()
    playerEnemy.isAttacking = false

    gsap.to("#playerHealth", {
      width: playerCharacter.health + "%"
    })
  }

  // If Enemy Misses
  if (playerEnemy.isAttacking && playerEnemy.framesCurrent === 2) {
    playerEnemy.isAttacking = false
  }

  // End Condition (Health)
  if (playerEnemy.health <= 0 || playerCharacter.health <= 0) {
    determineWinner({ playerCharacter, playerEnemy, timerId })
  }
}

animate()

window.addEventListener("keydown", (event) => {
  if (!playerCharacter.dead) {
    switch (event.key) {
      case "d":
        keys.d.pressed = true
        playerCharacter.lastKey = "d"
        break
      case "a":
        keys.a.pressed = true
        playerCharacter.lastKey = "a"
        break
      case "w":
        playerCharacter.velocity.y = -20
        break
      case " ":
        playerCharacter.attack()
        break
    }
  }

  if (!playerEnemy.dead) {
    switch (event.key) {
      case "ArrowRight":
        keys.ArrowRight.pressed = true
        playerEnemy.lastKey = "ArrowRight"
        break
      case "ArrowLeft":
        keys.ArrowLeft.pressed = true
        playerEnemy.lastKey = "ArrowLeft"
        break
      case "ArrowUp":
        playerEnemy.velocity.y = -20
        break
      case "ArrowDown":
        playerEnemy.attack()

        break
    }
  }
})

window.addEventListener("keyup", (event) => {
  switch (event.key) {
    case "d":
      keys.d.pressed = false
      break
    case "a":
      keys.a.pressed = false
      break
  }

  // playerEnemy keys
  switch (event.key) {
    case "ArrowRight":
      keys.ArrowRight.pressed = false
      break
    case "ArrowLeft":
      keys.ArrowLeft.pressed = false
      break
  }
})