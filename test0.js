const knn = require("./knn");

//console.log(knn.getType([1, 9, 8, 9, 2, 0, 1, 2, 6, 7, 8]));

let learningstyle;
//learningstyle = (knn.getType([1, 9, 8, 9, 2, 0, 1, 2, 6, 7, 8]));
learningstyle = (knn.getType([1,2,5,0,5,5,2,2,5,3,7]));

/*Position 1 active or reflective: a or r, 
Position 2: sensing or intuitive: s or i 
Position 3: visual or verbal: v or r 
Position 4 sequential or global: s or g,*/ 
console.log('The learning style according to the input is as follows: ');
console.log(learningstyle);
if(learningstyle=='rirs'){
    console.log('Reflective,Intitutive, Verbal,Sequential')
}
if(learningstyle=='airg'){
    console.log('Active,Intitutive, Verbal,Global')
}
if(learningstyle=='airs'){
    console.log('Active,Intitutive, Verbal,Sequential')
}
if(learningstyle=='aivg'){
    console.log('Active,Intitutive, Visual, Global')
}
if(learningstyle=='aivs'){
    console.log('Active,Intitutive, Visual, Sequential ')
}
if(learningstyle=='asrg'){
    console.log('Active,Sensing, Verbal, Global ')
}
if(learningstyle=='asrs'){
    console.log('Active,Sensing, Verbal, Sequential ')
}
if(learningstyle=='asvg'){
    console.log('Active,Sensing, Visual, Global')
}
if(learningstyle=='asvs'){
    console.log('Active,Sensing, Visual, Sequential')
}
if(learningstyle=='rirg'){
    console.log('Reflective,Intitutive, Verbal, Global')
}
if(learningstyle=='rivg'){
    console.log('Reflective,Intitutive, Visual, Global ')
}
if(learningstyle=='rivs'){
    console.log('Reflective,Intitutive, Visual, Sequential  ')
}
if(learningstyle=='rsrg'){
    console.log('Reflective,Sensing, Verbal, Global')
}
if(learningstyle=='rsrs'){
    console.log('Reflective,Sensing, Verbal, Sequential  ')
}
if(learningstyle=='rsvg'){
    console.log('Reflective,Sensing, Visual, Global ')
}
if(learningstyle=='rsvs'){
    console.log('Reflective,Sensing, Visual, Sequential ')
}

