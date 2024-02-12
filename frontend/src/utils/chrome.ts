export async function getUrl() {
    const [tab] = await chrome.tabs.query({active:true})
    return tab.url
    
}