function containerDim(selector, dim) {
    return parseInt(d3.select(selector).style(dim))
}

window.onload = function(){
var selector = '#map',
    width = containerDim(selector, 'width'),
    height = containerDim(selector, 'height');

//var projection = d3.geo.naturalEarth()
var projection = d3.geo.mercator()
    //.scale(width/20)
    //.translate([width / 10, height / 10])
    .scale(60)
    .translate([160, 100])
//    .translate([200, 800])
    ;

/*
var svg = d3.select(selector).append('svg')
    .attr('width', width)
    .attr('height', height);
*/

//d3.csv('/iploc.2.csv', function(error, data) {
d3.csv('/iploc.csv', function(error, data) {

var start = new Date().getTime();


/*
    svg.selectAll('rect')
        .data(data)
    .enter().append('svg:rect')
        .attr('transform', function(d) {
            return 'translate(' + projection([d.x, d.y]) + ')';
        })
        .attr('width', .8)
        .attr('height', .8);
console.log((new Date().getTime()) - start);
*/

    var ctx = document.getElementById('map').getContext('2d');
    data.forEach(function(d) {
        var proj = projection([d.x, d.y]);
        ctx.fillStyle = 'rgb(0,0,80)';
        ctx.fillRect(proj[0], proj[1], .091, .091);
    });

console.log((new Date().getTime()) - start);
});

};