(function(){
    'use strict';
    var counter = document.querySelector("#images_advertising").childNodes.length - 1;
    var counterTotal = counter;
    setInterval(function(){ 
        document.querySelector("#image_container_advertising_" + counter).style.display = 'none';
        document.querySelector("#img_advertising_" + counter).style.display = 'none';
        
        if(counter <= 0){
            counter = counterTotal;
            for(var i=0;i<=counter;i++){
                document.querySelector("#image_container_advertising_" + i).style.display = 'block';
                document.querySelector("#img_advertising_" + i).style.display = 'block';
            }
        }else{
            counter--;
        }
    }, 3000);
})();
