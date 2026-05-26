const calculator = document.querySelector(".calculator");
const keys = calculator.querySelector(".keys");

keys.addEventListener("click", event => 
    {
    if (event.target.matches("button")) 
        {
        const key = event.target;
        const action = key.dataset.action;
        }

    if (!action) 
    { console.log("number key!"); }

    if 
    (
        action === "add" ||
        action === "subtract" ||
        action === "multiply" ||
        action === "divide"
    ) 

    { console.log("operator key!"); }

    if (action === "decimal") 
        { console.log("decimal key!"); }

    if (action === "clear") 
        { console.log("clear key!"); }

    if (action === "calculate") 
        { console.log("equal key!"); }
});

const display = calculator.querySelector(".display");

keys.addEventListener("click", event =>
    {
    if (event.target.matches("button"))
        {
        const key = event.target;
        const action = key.dataset.action;
        const keyContent = key.textContent;
        const displayedNum = display.textContent;  
        }

    if (!action)
    {
        if (displayedNum === "0") {
            display.textContent = keyContent;
        } else {
            display.textContent = displayedNum + keyContent;
        }
    }

    if (action === "decimal")
    {
        if (!displayedNum.includes(".")) {
            display.textContent = displayedNum + ".";
        }
    }

    if 
    (
        action === "add" ||
        action === "subtract" ||
        action === "multiply" ||
        action === "divide"
    )
    {
        key.classList.add("is-depressed");
    }
});

key.addEventListener("click", event =>
    {
    if (event.target.matches("button"))
        {
        const key = event.target;
        const action = key.dataset.action;

        Array.from(key.parentNode.children).forEach(l => l.classList.remove("is-depressed"));
    }
});

key.addEventListener("click", event =>
    {
    if (event.target.matches("button"))
        {
        const key = event.target;
        const action = key.dataset.action;
        if (
            action === "add" ||
            action === "subtract" ||
            action === "multiply" ||
            action === "divide"
        ) {
            key.classList.add("is-depressed");
            calculator.dataset.previousKeyType = "operator"
        }
    }
    });

const previousKeyType = calculator.dataset.previousKeyType;

if (!action) 
    {
    if (displayedNum === "0" || previousKeyType === "operator") {
        display.textContent = keyContent;
    } else {
        display.textContent = displayedNum + keyContent;
    }
    }

if (action === "calculate") {
    const secondValue = displayedNum;
    const firstValue = calculator.dataset.firstValue;
    const operator = calculator.dataset.operator;
}

if (
    action === "add" ||
    action === "subtract" ||
    action === "multiply" ||
    action === "divide"
)
{
    calculator.dataset.firstValue = displayedNum;
    calculator.dataset.operator = action;
}

if (action === 'caltulcate') {
    const firrstValue = calculator.dataset.firstValue;
    const operator = calculator.dataset.operator;
    const secondValue = displayedNum;

    display.textContent = calculate(firstValue, operator, secondValue);
}

function calculate(n1, operator, n2) {
    let result = "";

    if (operator === "add") {
        result = parseFloat(n1) + parseFloat(n2);
    } else if (operator === "subtract") {
        result = parseFloat(n1) - parseFloat(n2);
    } else if (operator === "multiply") {
        result = parseFloat(n1) * parseFloat(n2);
    } else if (operator === "divide") {
        result = parseFloat(n1) / parseFloat(n2);
    }
    return result;
}