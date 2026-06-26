document.querySelectorAll('.dropdown').forEach(function (dropDownWrapper) {

    const dropDownBtn = dropDownWrapper.querySelector('.dropdown__button');
    const dropDownList = dropDownWrapper.querySelector('.dropdown__list');
    const dropDownListItems = dropDownWrapper.querySelectorAll('.dropdown__list-item');
    const dropDownInput = dropDownWrapper.querySelector('.dropdown__input-hidden');

    // Открыть/закрыть select по клику
    dropDownBtn.addEventListener('click', function () {
        dropDownList.classList.toggle('dropdown__list--visible');
        dropDownWrapper.querySelector('.caret').classList.toggle('caret--open');
    });

    // Ввод выбранного значения в основное поле
    dropDownListItems.forEach(function (listItem) {
        listItem.addEventListener('click', function (event) {
            event.stopPropagation();
            dropDownBtn.innerText = this.innerText;
            dropDownList.classList.remove('dropdown__list--visible');
            dropDownWrapper.querySelector('.caret').classList.remove('caret--open');
            dropDownInput.value = this.dataset.value;
        });
    });

    // Закрытие списка при нажатии на другие элементы
    document.addEventListener('click', function (event) {
        if (event.target !== dropDownBtn) {
            dropDownList.classList.remove('dropdown__list--visible');
            dropDownWrapper.querySelector('.caret').classList.remove('caret--open');
        }
    });

    // Закрытие списка при нажатии на Tab или Escape
    document.addEventListener('keydown', function (event) {
        if (event.key === 'Tab' || event.key === 'Escape') {
            dropDownList.classList.remove('dropdown__list--visible');
        }
    });

});


