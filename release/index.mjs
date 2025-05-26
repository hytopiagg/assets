import { readFileSync } from 'fs';

export default {
  dev: {
    ssl: {
      cert: readFileSync(new URL('./certs/localhost.crt', import.meta.url), 'utf8'),
      key: readFileSync(new URL('./certs/localhost.key', import.meta.url), 'utf8'),
    },
  }
}