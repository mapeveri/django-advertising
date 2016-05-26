(function()
{
    'use strict';
    var counter = document.querySelector("#images_advertising").childNodes.length - 1;
    var counterTotal = counter;
    var container, image;

    //This variable to load template tag
    var secondsIntervalAdvertising;
    if(window.TimeOutAdvertising)
    {
        secondsIntervalAdvertising = window.TimeOutAdvertising;
    }else
    {
        secondsIntervalAdvertising = 3000;
    }

    setInterval(function()
    {
        //Hide image index counter
        if (counter > -1)
        {
            toogle(counter, false);
        }

        //If the final, again show images
        if(counter <= 0)
        {
            counter = counterTotal;
            for(var i=0;i<=counter;i++)
            {
                toogle(i, true);
            }
        }else
        {
            counter--;
        }
    }, secondsIntervalAdvertising);

    /**
     * @name: toogle
     * @descrip: Check if is show or hide elements image and container
     * @param {Integer} counter - id element.
     * @param {Boolena} is_show - if element is show or hide
    */
    function toogle(counter, is_show)
    {
        container = "#image_container_advertising_" + counter;
        image = "#img_advertising_" + counter;

        if(is_show)
        {
            displayMe(document.querySelector(container));
            displayMe(document.querySelector(image));
        }else{
            hideMe(document.querySelector(container));
            hideMe(document.querySelector(image));
        }
    }

    /**
     * @name: displayMe
     * @descrip: Show element of the dom.
     * @param {htmlElement} element - Element to show.
    */
    function displayMe(element)
    {
        element.style.transition = "all .3s";
        element.style.opacity = "1";
    }

    /**
     * @name: hideMe
     * @descrip: Hide element of the dom.
     * @param {htmlElement} element - Element to hide.
    */
    function hideMe(element)
    {
        element.style.transition = "all .3s";
        element.style.opacity = "0";
    }

})();
