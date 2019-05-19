export = index;
declare class index {
  static buildRequest(e: any): any;
  static clearCache(): void;
  static execute(e: any): any;
  static http(e: any, ...args: any[]): any;
  static makeApisTagOperation(...args: any[]): any;
  static makeHttp(p0: any, p1: any): any;
  static parameterBuilders: any;
  static resolve(e: any): any;
  static resolveSubtree(e: any, r: any, ...args: any[]): any;
  static serializeHeaders(...args: any[]): any;
  static serializeRes(e: any, t: any, ...args: any[]): any;
  constructor(e: any, ...args: any[]);
  applyDefaults(): void;
  execute(e: any): any;
  http(e: any, ...args: any[]): any;
  resolve(): any;
}
declare namespace index {
  namespace helpers {
    function opId(e: any, t: any, ...args: any[]): any;
  }
}
