client = new Paho.MQTT.Client('test.mosquitto.org', Number(8080), "clientId");

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({onSuccess:onConnect});


function onConnect() {
    console.log("onConnect");
    client.subscribe("World");
}

//ส่งข้อความ
function sendMessage(topic,text){
    message = new Paho.MQTT.Message(text);
    message.destinationName = topic;
    client.send(message);
}

// เชื่อมต่อไม่สำเร็จ
function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:"+responseObject.errorMessage);
    }
}
// รับข้อความ
function onMessageArrived(message) {
    console.log(message.payloadString);
}

/*
setTimeout(()=>{
    document.getElementById('loading').classList.remove('image-animation');
    document.getElementById('loading').classList.add('fade-out');
    setTimeout(()=>{
        document.getElementById('loading').classList.remove('fade-out');
        document.getElementsByClassName('loading')[0].style.display = 'none'
        document.getElementsByClassName('main-process')[0].style.display = 'block'
        setTimeout(()=>{
            document.getElementsByClassName('nav')[0].style.top = '0px'
        },500)
    },1000)
}, 3000)*/

document.getElementsByClassName('nav')[0].style.top = '0px'

var scene, camera, renderer;
            var geometry, material, mesh;
            var width=1024, height=768;
            var viewAngle = 75;
            var aspect = width/height;
            var near = 1, far=10000;
            
            scene = new THREE.Scene();

                camera = new THREE.PerspectiveCamera( viewAngle, aspect, near, far);
                
                geometry = new THREE.BoxGeometry(200, 300, 200);
                material = new THREE.MeshBasicMaterial( { color: 0xff0000, wireframe: true } );

                mesh = new THREE.Mesh( geometry, material );
                //scene.add( mesh );

                renderer = new THREE.WebGLRenderer({ antialias : true });
                renderer.setSize( (window.innerWidth*70)/100, window.innerHeight );
                renderer.setClearColor( 0xFFFFFF, 1);
                document.getElementsByClassName('main-right')[0].appendChild( renderer.domElement );
                renderer.render( scene, camera );
            
            var obj = null
            const loader = new THREE.GLTFLoader()
            loader.load(
                'scene.glb',
                function (gltf) {
                    obj = gltf
                    obj.scene.rotation.y = -5
                    obj.scene.position.z = -1500
                    obj.scene.position.x = 100
                    obj.scene.position.y = -200
                    // obj.scene.rotation.x = 10
                    gltf.scene.traverse(function (child) {
                      camera.position.y = 550
                        
                      
                    })
                    scene.add(gltf.scene)
                },
                (xhr) => {
                    console.log((xhr.loaded / xhr.total) * 100 + '% loaded')
                },
                (error) => {
                    console.log(error)
                }
            )
            
            document.addEventListener('keydown',(e)=>{
              console.log(e.key,e.key == 'a')
              if(e.key == 'a'){
                //sendMessage('BURL/MOVE','a')
                //obj.scene.rotation.y += 0.01
                obj.scene.position.y += 0.01
                camera.scene.position.y += 0.01

              }else if(e.key == 'd'){
                //sendMessage('BURL/MOVE','d')
                obj.scene.position.y -= 0.01
                camera.scene.position.y -= 0.01
                //obj.scene.rotation.y -= 0.01
              }else if(e.key == 'w'){
                //sendMessage('BURL/MOVE','w')
                obj.scene.position.y += 0.5
                camera.scene.position.x += 0.01
              }else if(e.key == 's'){
                //sendMessage('BURL/MOVE','s')
                obj.scene.position.z -= 0.5
              }else if(e.key == 'x'){
                //sendMessage('BURL/MOVE','s')
                obj.scene.position.z -= 0.5
                camera.scene.position.x -= 0.01
              }
              
              renderer.render( scene, camera );
            })
            const directionalLight = new THREE.DirectionalLight( 0xDDDDDD, 2 );
				    directionalLight.position.set( 0, 0, 0 );
				    scene.add( directionalLight );
            setInterval(()=>{
              mesh.rotation.y += 0.02;
              
              renderer.render( scene, camera );
            },100)
// document.getElementById('fall_btn').onclick(document.getElementById('fall_btn').style.backgroundColor='red');
// document.getElementById('w_btn').addEventListener('click',sendMessage('TEST/MQTT','move-w'));