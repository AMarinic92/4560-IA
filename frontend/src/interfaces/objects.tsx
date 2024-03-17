export interface Problem{
    id:string|number
    type:string 
    imageUrl:string
    message:string
    suggestion:string
}

export interface Suggestion{
    id:string      // should probably be the same ID as its matching problem
    type:string
    message: string
}