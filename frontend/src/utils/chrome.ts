
function getImageID(src:string){
    return src
}



export async function getUrl() {
    const [tab] = await chrome.tabs.query({active:true})
    return tab.url
    
}




export async function showImage(src:string) {
    const [tab] = await chrome.tabs.query({active:true})
   // const id =getImageID(src)
   // console.log(id)
    chrome.scripting.executeScript({
        target:{tabId:tab.id!},
        func:()=>{
            const images = document.querySelectorAll(`img[src="${src}"]`)
            images.forEach(image => {
                console.log(image)
              });
        }
    })
}