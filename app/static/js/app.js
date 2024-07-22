$(document).ready(function() {
    $("#city-input").autocomplete({
        autoFocus: true,
        delay: 500,
        minLength: 3,
        source: function(request, response) {
            $.ajax({
                url: "/autocomplete",
                data: { q: request.term },
                success:function(data) {
                    response(data["cities"])
                },
                error: function() {
                  response([]);
                }
            })
        },
    });
    function showTempCiti(citi_name){
        $.ajax({
                url: `/weather?city=${citi_name}`,
                success: function(data) {
                    $("#weather-result").html("");
                    const template = document.getElementById('weather-template').content.cloneNode(true);
                    template.querySelector('.city-name').textContent = data.name;
                    template.querySelector('.temperature').textContent = data.current_temp;
                    template.querySelector('.wind-speed').textContent = data.wind_speed;
                    template.querySelector('.description').textContent = data.description;

                    document.getElementById('weather-result').appendChild(template);


                    if (!lastCities.includes(city)) {
                        lastCities.unshift(city);
                        if (lastCities.length > 5) {
                            lastCities.pop();
                        }
                        localStorage.setItem('lastCities', JSON.stringify(lastCities));
                    }
                },
                error: function(xhr) {
                    $("#weather-result").html(`<p>Error: ${xhr.responseJSON.detail}</p>`);
                }
            });
    }
     $("#weather-form").on("submit", function(event) {
            event.preventDefault();

            const city = $("#city-input").val();
            showTempCiti(city)
        });
    const lastCities = JSON.parse(localStorage.getItem('lastCities')) || [];
    const container =  document.getElementById('last-cities')
    lastCities.map((value)=>{
        let button = document.createElement("button")
        button.classList.add("btn")
        button.classList.add("btn-link")
        button.textContent=value
        button.setAttribute("data-value",value)
        button.onclick=function(e){
            let element = e.target
            $('#city-input').val(element.getAttribute("data-value"));
            showTempCiti(element.getAttribute("data-value"))
        }
        container.appendChild(button);
    })

});