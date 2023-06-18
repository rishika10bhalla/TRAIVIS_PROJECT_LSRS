const knn = require("./knn");


function eval(a,b,c,d,e,f,g,h,i,j,k) {
    learningstyle = (knn.getType([a,b,c,d,e,f,g,h,i,j,k]));
    return learningstyle;
}
  
  // Access the arguments passed from the Python script
  var arg1 = parseInt(process.argv[2]);
  var arg2 = parseInt(process.argv[3]);
  var arg3 = parseInt(process.argv[4]);
  var arg4 = parseInt(process.argv[5]);
  var arg5 = parseInt(process.argv[6]);
  var arg6 = parseInt(process.argv[7]);
  var arg7 = parseInt(process.argv[8]);
  var arg8 = parseInt(process.argv[9]);
  var arg9 = parseInt(process.argv[10]);
  var arg10 = parseInt(process.argv[11]);
  var arg11 = parseInt(process.argv[12]);
  
  // Call the function and store the result
  var result = eval(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
  
  // Print the result
  console.log('The learning style according to the input is as follows:   ');
  //console.log('Learning Style : ', result);
  

/*Position 1 active or reflective: a or r, 
Position 2: sensing or intuitive: s or i 
Position 3: visual or verbal: v or r 
Position 4 sequential or global: s or g,*/ 

if(learningstyle=='rirs'){
    console.log('Reflective,\n Intitutive,\n Verbal,\nSequential')
}
if(learningstyle=='airg'){
    console.log('Active,\nIntitutive,\n Verbal,\nGlobal')
}
if(learningstyle=='airs'){
    console.log('Active,\nIntitutive,\n Verbal,\nSequential')
}
if(learningstyle=='aivg'){
    console.log('Active,\nIntitutive,\n Visual, \nGlobal')
}
if(learningstyle=='aivs'){
    console.log('Active,\nIntitutive,\n Visual,\n Sequential ')
}
if(learningstyle=='asrg'){
    console.log('Active,\nSensing,\n Verbal,\n Global ')
}
if(learningstyle=='asrs'){
    console.log('Active,\nSensing,\n Verbal,\n Sequential ')
}
if(learningstyle=='asvg'){
    console.log('Active,\nSensing, \nVisual,\n Global')
}
if(learningstyle=='asvs'){
    console.log('Active,\nSensing,\n Visual, \nSequential')
}
if(learningstyle=='rirg'){
    console.log('Reflective,\nIntitutive,\n Verbal,\n Global')
}
if(learningstyle=='rivg'){
    console.log('Reflective,\nIntitutive, \nVisual,\n Global ')
}
if(learningstyle=='rivs'){
    console.log('Reflective,\nIntitutive,\n Visual, \nSequential  ')
}
if(learningstyle=='rsrg'){
    console.log('Reflective,\nSensing, \nVerbal,\n Global')
}
if(learningstyle=='rsrs'){
    console.log('Reflective,\nSensing,\n Verbal,\n Sequential  ')
}
if(learningstyle=='rsvg'){
    console.log('Reflective,\nSensing,\n Visual,\n Global ')
}
if(learningstyle=='rsvs'){
    console.log('Reflective,\nSensing,\n Visual,\n Sequential ')
}

