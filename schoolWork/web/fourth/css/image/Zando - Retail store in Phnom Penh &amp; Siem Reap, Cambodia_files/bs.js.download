// Copyright (c) 2022 Ivan Teplov
document.body.insertAdjacentHTML(
  'beforeend',
  `
<div id="aba_checkout_sheet" class="aba_checkout_column aba_checkout_items_center aba_checkout_justify_end" aria-hidden="true">
<!-- Dark background for the sheet -->
<div class="aba_checkout_overlay"></div>

<!-- The sheet itself -->
<div class="aba_checkout_contents aba_checkout_column">
<!-- Sheet controls -->
<header>
  <!-- The thing to drag if you want to resize the sheet -->
  <div class="aba_checkout_draggable_area">
    <div class="aba_checkout_draggable-thumb"></div>
  </div>
</header>

<!-- Body of the sheet -->
<main class="aba_checkout_column" id="aba_checkout_app">
</main>
</div>
</div>`
)

const abaCheckoutSheet = document.querySelector('#aba_checkout_sheet')
const abaCheckoutSheetContents = abaCheckoutSheet.querySelector('.aba_checkout_contents')
const abaCheckoutDraggableArea = abaCheckoutSheet.querySelector('.aba_checkout_draggable_area')

let abaCheckoutSheetHeight // in vh
let abaCheckoutOffsetDragDown // in vh

const abaCheckoutSetSheetHeight = (value) => {
  abaCheckoutSheetHeight = value
  // abaCheckoutSheetContents.style.minHeight = `416px`;
  abaCheckoutSheetContents.style.height = `${value}px`

  // if (abaCheckoutSheetHeight === 100) {
  //   abaCheckoutSheetContents.classList.add("fullscreen");
  // } else {
  //   abaCheckoutSheetContents.classList.remove("fullscreen");
  // }
}

const abaCheckoutSetIsSheetShown = (value) => {
  abaCheckoutSheet.setAttribute('aria-hidden', String(!value))
}

// Hide the sheet when clicking the background
abaCheckoutSheet.querySelector('.aba_checkout_overlay').addEventListener('click', () => {
  abaCheckoutSetSheetHeight(100)
  abaCheckoutSetIsSheetShown(false)
  abaCheckoutOffsetDragDown = 0
  document.body.style.overflowY = 'auto' // open scroll body
})

const abaCheckoutTouchPosition = (event) => (event.touches ? event.touches[0] : event)

let abaCheckoutDragPosition

const abaCheckoutOnDragStart = (event) => {
  abaCheckoutDragPosition = abaCheckoutTouchPosition(event).pageY
  abaCheckoutSheetContents.classList.add('not-selectable')
  abaCheckoutDraggableArea.style.cursor = document.body.style.cursor = 'grabbing'
}

const abaCheckoutOnDragMove = (event) => {
  if (abaCheckoutDragPosition === undefined) return

  const y = abaCheckoutTouchPosition(event).pageY
  const deltaY = abaCheckoutDragPosition - y
  const deltaHeight = (deltaY / window.innerHeight) * 100
  abaCheckoutOffsetDragDown = deltaHeight
  if (abaCheckoutOffsetDragDown < 0) {
    abaCheckoutSetSheetHeight(abaCheckoutSheetHeight + deltaHeight)
  }
  abaCheckoutDragPosition = y
}

const abaCheckoutOnDragEnd = () => {
  abaCheckoutDragPosition = undefined
  abaCheckoutSheetContents.classList.remove('not-selectable')
  abaCheckoutDraggableArea.style.cursor = document.body.style.cursor = ''

  if (abaCheckoutOffsetDragDown < -1) {
    abaCheckoutSetSheetHeight(100)
    abaCheckoutSetIsSheetShown(false)
    abaCheckoutOffsetDragDown = 0
    document.body.style.overflowY = 'auto' // open scroll body
  } else {
    abaCheckoutSetSheetHeight(abaCheckoutSheetHeight)
  }
}

abaCheckoutDraggableArea.addEventListener('mousedown', abaCheckoutOnDragStart)
abaCheckoutDraggableArea.addEventListener('touchstart', abaCheckoutOnDragStart)

window.addEventListener('mousemove', abaCheckoutOnDragMove)
window.addEventListener('touchmove', abaCheckoutOnDragMove)

window.addEventListener('mouseup', abaCheckoutOnDragEnd)
window.addEventListener('touchend', abaCheckoutOnDragEnd)
