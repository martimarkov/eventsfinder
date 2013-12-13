var add_event = {
    init : function() {
        $("#find-location-button").bind("click", function lookupGeoData() {
            console.log("here");
            myGeoPositionGeoPicker({
                startAddress     : 'White House, Washington',
                returnFieldMap   : {
                    'add-event-form-lat' : '<LAT>',
                    'add-event-form-long' : '<LNG>',
                    'add-event-form-city' : '<CITY>',
                    'add-event-form-country' : '<COUNTRY>',
                    'add-event-form-zip' : ' <ZIP>',
                    'add-event-form-address' : '<ADDRESS>'
                }
            });
        });

        $('#end-datetime, #start-datetime').datetimepicker({
            format: 'dd/MM/yyyy hh:mm:ss',
            language: 'en-GB'
        });
    }
}

$(function() {
    add_event.init();
})();