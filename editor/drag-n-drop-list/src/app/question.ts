export class Question {
    constructor(
        public id: number,
        public content: string,
        public triggers: Array<string>,
        public outputs: Array<string>
    ){}
}
