
/**
 * checker
 * sends url of page to backend to be processed and return issues and solutions
 * @url , string of tab url ,this is null if url is null
 * @returns solutions and accessibility issues of a web page
 */
export async function checker(url :string|null|undefined) {
    // implementation to talk to the cluster
     // if url is null something went wrong when getting a tab url
    if(!url){
       console.log(url)

    }

    return null;
    
}