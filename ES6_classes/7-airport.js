export default class Airport {
    constructor(name, code) {
        this._name = name;
        this._code = code;
    }

    get [symbol.toStringTag]() {
        return this._code;
    }
}
