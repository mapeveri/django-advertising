(function(){
    'use strict';
    var counter = document.querySelector("#images_advertising").childNodes.length - 1;
    var counterTotal = counter;
    var classe = 'transition-advertising';
    setInterval(function(){ 
        //Hide image index counter
        document.querySelector("#image_container_advertising_" + counter).classList.add(classe);
        document.querySelector("#img_advertising_" + counter).classList.add(classe);
        
        //If the final, again show images
        if(counter <= 0){
            counter = counterTotal;
            for(var i=0;i<=counter;i++){
                document.querySelector("#image_container_advertising_" + i).classList.remove(classe);
                document.querySelector("#img_advertising_" + i).classList.remove(classe);
            }
        }else{
            counter--;
        }
    }, 3000);
})();
